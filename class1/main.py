import requests
import json
import streamlit as st

st.title("demo app")
st.write("ask your question")

input=st.text_input("ask qustions")
if input is not None:
    btn=st.button("submit")
    if btn:

      url = "https://api.openai.com/v1/chat/completions"

      payload = json.dumps({
        "model": "gpt-4o",
        "messages": [
          {
            "role": "system",
            "content": "you are an expert in devops with aws knowledge with 15 years experience?"
          },
          {
            "role": "user",
            "content": input
          }
        ]
      })
      headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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',
        'Cookie': '__cf_bm=PFa9tcZnbhBFfNNwzaqB5wAim9Li6AvocTBiPaJjauc-1720357853-1.0.1.1-R2hGlpJCr.ZLsoPAGUiEPHIvQ1LxAm42k.CzBfpzIShpjtzcPu806bhF1avxpecTAJmvyu0Rt_hTB4QjmoHVxQ; _cfuvid=SGx7QkcmyseNdpN0ADUkl5vRFzPWfv.si6SOsUNSDDU-1720357853102-0.0.1.1-604800000'
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      data=response.json()
      st.write(data["choices"][0]["message"]["content"])
