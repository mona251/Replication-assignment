import json
import argparse
import subprocess

from utils import *
from ollama import chat

def extract_code(text: str) -> str:
    pattern = r"```(?:python)?\s*(.*?)```"
    return re.findall(pattern, text, re.DOTALL)

def send_message(model: str, messages: list, module: str):
    try:
        response = chat(model, messages=[*messages[:-2], messages[-1]])    
    except:
        subprocess.run(['ollama', 'pull', model])
        response = chat(model, messages=[*messages[:-2], messages[-1]]) 
    code = extract_code(response.message.content)   
    filename = get_unique_filename(module)
    with open(f'{filename}', 'w') as f:
        f.write(''.join(code))
    print(response.message.content)
    
if __name__ == '__main__':
    
    with open('./prompt_templates.json', 'r') as f:
        prompt_templates = json.load(f)
    
    modules = [f for f in os.listdir('.') if not f.startswith('.') and os.path.isdir(f) and f != '__pycache__']
    
    parser = argparse.ArgumentParser(description="add model")
    parser.add_argument("--model", type=str, default='mistral-small3.1:latest')
    args = parser.parse_args()
    
    model = args.model
    
    for module in modules:
        print(f"Generating test cases for {module}...")
        if os.path.exists(f'./{module}/params.json'):
            with open(f'./{module}/params.json', 'r') as f:
                params = json.load(f)
        
        import_statements, test_file_content, module_file_content = extract_file_contents(module)
        M = len(module_file_content)
        test_cases = extract_test_cases(test_file_content, params['test_cases'])
        prompts = build_prompts(prompt_templates, import_statements, test_file_content, module_file_content, test_cases, M)
        messages = [dict(role = 'user', content = prompt) for prompt in prompts]
        send_message(model, messages, module)
        
        
    
    
    
    
        

        
        

        
        
                
    
    
    


    
