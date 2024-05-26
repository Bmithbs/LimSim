import yaml
import os
from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

CONFIG = yaml.load(open('api_config.yaml'), Loader=yaml.FullLoader)
os.environ["OPENAI_API_KEY"] = CONFIG['OPENAI']['api_key']
os.environ["OPENAI_API_BASE"] = CONFIG['OPENAI']['api_base']

# 创建 ChatOpenAI 实例
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.7)

# 定义一个 PromptTemplate
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="You are a helpful assistant. Respond to the following user input:\n\n{user_input}"
)

# 创建一个 LLMChain 实例
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

def get_response(user_input):
    # 调用 LLMChain 生成回复
    response = llm_chain.run({"user_input": user_input})
    return response



if __name__ == '__main__':
    
    while True:
        # 获取用户输入
        user_input = input("You: ")
        
        # 退出条件
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        
        # 获取并打印回复
        response = get_response(user_input)
        print(f"Bot: {response}")
    