import os
import win32api


def print_all_pdfs_in_folder(folder_path):
    file_list = os.listdir(folder_path)
    pdf_files = [f for f in file_list if f.lower().endswith(".pdf")]
    if not pdf_files:
        print("没有可以打印的文件")
        return
    
    for pdf_file in pdf_files:
        pdf_file_path = os.path.join(folder_path,pdf_file)
        try:
            #subprocess.run(["C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe","/p",pdf_file_path],shell=True) 
            win32api.ShellExecute(0,"print",pdf_file_path,None,".",0)
            print(f"已打印文件：{pdf_file}")
        except Exception as e:
            print(f"打印文件时出错：{e}")

if __name__ == "__main__":
    folder_path = "D:/Work/石宝山公司/2023年/发票存档/六安/7月"
    print_all_pdfs_in_folder(folder_path)