from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
for char in 'abcdefghijklmnopqrstuvwxyz':
    for char2 in 'abcdefghijklmnopqrstuvwxyz':
        test_password = char + char2 + 'bcmpda'
        print(f"Trying password: {test_password}")
        if unzip_with_7z(zip_file_path, dest_path, test_password):
            print(f"The secret password is: {test_password}")
            break
    else:
        continue
    break