import time

from gateway.gateway import LmStudioGateway

address = "http://localhost:1234/v1"

class OutputPerModel:
    def __init__(self, model_name: str):
        self.gateway = LmStudioGateway(url=address, model_name=model_name)
        self.responses = []
    def append(self, response: str):
        self.responses.append(response)

class ComparingResults:
    def __init__(self, system_prompt: str, user_prompt: str, model_names: list[str]):
        self.outputs = [OutputPerModel(model_name) for model_name in model_names]
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt

if __name__ == "__main__":

    system_prompt = """貴方はプロの小説家です。以下のユーザのアイデアをもとに、魅力的な小説の冒頭文を生成してください。"""
    user_prompt = "ユーザのアイデア：かつて星は、夢をみた。"
    model_names = [""]

    comparing_results = ComparingResults(system_prompt, user_prompt, model_names)

    for output in comparing_results.outputs:
        start_time = time.time()
        for i in range(5):
            print(f"Generating response {i + 1} for model {output.gateway.model_name}...")
            response = output.gateway.response(system=system_prompt, user=user_prompt)
            output.append(response)
        print(f"Finished generating responses for model {output.gateway.model_name}.")
        end_time = time.time()
        print(f"Time taken for model {output.gateway.model_name}: {end_time - start_time:.2f} seconds")

    # csvファイルに保存する
    csv_file_path = "comparing_results.csv"
    with open(csv_file_path, mode='w', encoding='utf-8') as csv_file:
        csv_file.write("Model,Response\n")
        for output in comparing_results.outputs:
            for response in output.responses:
                csv_file.write(f"{output.gateway.model_name},{response.replace('\n', ' ')}\n")

    for output in comparing_results.outputs:
        print(f"Model: {output.gateway.model_name}")
        for i, response in enumerate(output.responses):
            print(f"""
                  ------------Response {i + 1}----------------
                  {response}
                  --------------------------------------------
                  """)
        print("-" * 50)