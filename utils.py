import os
import re
import parso

def get_unique_filename(module: str) -> str:
    base_filename = f"./{module}/test_{module}_improved"
    if not os.path.exists(base_filename + '.py'):
        return base_filename + '.py'

    counter = 2
    while True:
        new_filename = f"{base_filename}_{counter}.py"
        if not os.path.exists(new_filename):
            return new_filename
        counter += 1

def extract_file_contents(module: str):
    directory = f'./{module}/'
    current_module_dir = os.listdir(directory)
       
    with open(directory + f'test_{module}.py') as f:
        test_file_content = f.read() #store test file
        
    #Import statements
    import_pattern = re.compile(r'^\s*(import\s+[^\n]+|from\s+\S+\s+import\s+[^\n]+)', re.MULTILINE)
    imports = import_pattern.findall(test_file_content)
    import_statements = '\n'.join([stmt for stmt in imports])
    
    pattern = re.compile(r'import\s+([\w.]+)\s+as\s+module_\d+')
    extracted_modules = pattern.findall(import_statements)
    
    module_file_content = []
    for module_path in extracted_modules:
        module_path = module_path.replace('.', '/')
        try:
            with open(f'{directory}{module_path}.py') as f:
                module_file_content.append(f.read()) #store module source code
        except:
            break
            
    return import_statements, test_file_content, module_file_content

def extract_test_cases(test_file_content: str, test_cases: int):
    module = parso.parse(test_file_content)
    functions = []

    for node in module.children:
        if node.type == 'funcdef':
            func_code = node.get_code()
            functions.append(func_code)
    
    if test_cases == -1:
        return functions
    else:
        return functions[:test_cases]

def build_prompts(prompt_templates, import_statements, 
                  test_file_content, module_file_content, test_cases, M):
    
    if M == 1:
        templates = ["[module-under-test]", "{import statements}", "{test code}"]
        contents = [module_file_content[0], import_statements, test_cases]
        temp_vars = ['single_module', 'unit_test', 'test_cases']
    else:
        templates = ["[module-under-test]", "[module]", "{import statements}", "{test code}"]
        contents = [module_file_content[0], module_file_content[1:], import_statements, test_cases]
        temp_vars = ['multiple_modules_1', 'multiple_modules_2', 'unit_test', 'test_cases']
    prompt_templates[temp_vars[0]] = prompt_templates[temp_vars[0]].replace('{M}', str(M))
    
    prompts = []
    
    for template, content, temp_var in zip(templates, contents, temp_vars):
        if M == 1:
            if template == "{test code}":
                for test_case in content:
                    prompt = prompt_templates[temp_var].replace(template, '\n ``` \n' + test_case + '```')
                    prompts.append(prompt)
            else:
                prompt = prompt_templates[temp_var].replace(template, '\n ``` \n' + content + '```')
                prompts.append(prompt)
        else:
            if template == "[module]":
                for module_file in content:
                    prompt = prompt_templates[temp_var].replace(template, '\n ``` \n' + module_file + '```')
                    prompts.append(prompt)
            if template == "{test code}":
                for test_case in content:
                    prompt = prompt_templates[temp_var].replace(template, '\n ``` \n' + test_case + '```')
                    prompts.append(prompt)
            elif template == "[module-under-test]" or template == "{import statements}":
                prompt = prompt_templates[temp_var].replace(template, '\n ``` \n' + content + '```')
                prompts.append(prompt)
        
    prompts.append(prompt_templates['test_suite'])
    
    return prompts