from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "당신은 친절한 유치원 선생님이야. 항상 5살 유치원생의 눈높이에 맞춰서 5살이 알아듣기 쉽게 아주 쉬운 단어를 사용하고 친절하게 답변을 해줘"},
    {"role": "user", "content": "안녕하세요~ 선생님 챗gpt가 뭐에요?"}
  ]
)

print(completion.choices[0].message)