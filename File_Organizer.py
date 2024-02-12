import os
import shutil

sor=input(r"Enter the source dir path:").replace('\\','/')

dest=input(r"Enter the destinartion dir path").replace('\\','/')

extension_map={
    '.jpg':'Images',
    '.jpeg':'Images',
    '.jfif':'Images',
    '.mp3':'Videos',
    '.docx':'MS OFFICE',
    '.pptx':'MS OFFICE',
    '.pdf':'PDF'
}

for folder_name in set(extension_map.values()):
    os.makedirs(os.path.join(dest,folder_name),exist_ok=True)
    
for filename in os.listdir(sor):
    file_ext=os.path.splitext(filename)[-1].lower()
    
    
    if file_ext in extension_map:
        
        src_path=os.path.join(sor,filename)
        
        dest_path=os.path.join(dest,extension_map[file_ext],filename)
        shutil.move(src_path,dest_path)
        print("Files are now Organized......")