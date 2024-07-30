import ollama
import glob
import os


def action_analyzer_prompt():
    prompt = """
あなたにはサッカーの試合映像から、選手のアクションを分析する能力があります。
サッカーの試合映像を見て、選手のアクションを分析してください。

アクションには以下の種類があります。

1. パス
2. シュート
3. クロス
4. ドリブル
5. 成功したタックル
6. ハイパス
7. ヘッド

"""

    return prompt

def get_response(img_path, prompt):
    response = ollama.chat(
        model = "llava",
        messages = [
            {
                "role": "user",
                "content": prompt,
                "content": [img_path]
            }
        ]
    )

    return response["messages"]["content"]


def get_img_path_list(img_folder):
    img_path_list  = glob.glob(os.path.join(img_folder, '*'))
    img_path_list.sort()
    return img_path_list

def main():
    img_folder = "data/output/"
    img_path_list = get_img_path_list(img_folder)
    prompt = action_analyzer_prompt()

    for i, img_path in enumerate(img_path_list):
        print(f"target path: {img_path}")
        response = get_response(img_path, prompt)
        print(f"Frame{i}: {response}")

if __name__ == "__main__":
    main()