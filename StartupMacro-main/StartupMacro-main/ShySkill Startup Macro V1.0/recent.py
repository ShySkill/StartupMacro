file_path = r"C:\Users\ShySkill\Downloads\StartupMacro-main\StartupMacro-main\ShySkill Startup Macro V1.0\linktoserver.txt"

try:
    file = open(file_path, "r", encoding='utf-8')
    content = file.read()
    
    print("File contents (visible):\n" + content)
    
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)
finally:
    if 'file' in locals():
        file.close()
