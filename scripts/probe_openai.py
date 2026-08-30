#!/usr/bin/env python3
"""Bounded OpenAI-compatible capability probe (stdlib only)."""
import argparse, json, time, urllib.request


def post(url, body, timeout=300):
    req=urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type":"application/json"})
    started=time.monotonic()
    with urllib.request.urlopen(req, timeout=timeout) as response:
        data=json.load(response)
    return data, round(time.monotonic()-started, 3)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--base-url", required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--output", required=True)
    a=p.parse_args()
    endpoint=a.base_url.rstrip("/")+"/chat/completions"
    common={"model":a.model,"temperature":0,"max_tokens":128,"chat_template_kwargs":{"enable_thinking":False}}
    evidence={"schema":1,"model":a.model,"tests":{}}

    body={**common,"messages":[{"role":"user","content":"Reply exactly: BERTHOLOMUSAI_EXACT_OK"}]}
    data,seconds=post(endpoint,body)
    text=(data["choices"][0]["message"].get("content") or "").strip()
    evidence["tests"]["exact"]={"pass":text=="BERTHOLOMUSAI_EXACT_OK","seconds":seconds,"completion_tokens":data.get("usage",{}).get("completion_tokens")}

    tools=[{"type":"function","function":{"name":"add","description":"Add two integers","parameters":{"type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"],"additionalProperties":False}}}]
    body={**common,"messages":[{"role":"user","content":"Use add to calculate 17 + 25."}],"tools":tools,"tool_choice":"auto"}
    data,seconds=post(endpoint,body)
    calls=data["choices"][0]["message"].get("tool_calls") or []
    ok=False
    if calls:
        f=calls[0].get("function",{})
        try: ok=f.get("name")=="add" and json.loads(f.get("arguments","{}"))=={"a":17,"b":25}
        except json.JSONDecodeError: pass
    evidence["tests"]["tool_call"]={"pass":ok,"seconds":seconds}

    body={**common,"messages":[{"role":"user","content":"Return only this JSON object: {\"status\":\"ok\",\"value\":42}"}],"response_format":{"type":"json_object"}}
    data,seconds=post(endpoint,body)
    text=data["choices"][0]["message"].get("content") or ""
    try: parsed=json.loads(text); ok=parsed=={"status":"ok","value":42}
    except json.JSONDecodeError: ok=False
    evidence["tests"]["json"]={"pass":ok,"seconds":seconds}

    evidence["all_pass"]=all(x["pass"] for x in evidence["tests"].values())
    with open(a.output,"w") as f: json.dump(evidence,f,indent=2)
    print(json.dumps(evidence))
    raise SystemExit(0 if evidence["all_pass"] else 1)

if __name__=="__main__": main()
