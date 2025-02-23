
# Reading data from a text file
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of the file:\n{content}.\n")
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.\n")
        return None

# Writing user data to a new text file
def write_file(file_name, user_data):
    try:
        i=input("do you want to overwrite the file content ? y/n: ")
        if i=='y':
            with open(file_name, 'w') as file:
                file.write(user_data)
                print(f"Data has been written to '{file_name}'.\n")
                user=read_file('user_data.txt')
        else:
            with open(file_name, 'a') as file:
                file.write(user_data)
                print(f"Data has been appended to '{file_name}'.\n")
                u=read_file('user_data.txt')
            
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def main():
   
    input_file = "sample_text.txt"
    content = read_file(input_file)
    
    print("data present on 'user_data.txt' before writing or appending:\n")
    user=read_file('user_data.txt')
    if content is not None:
        output_file = "user_data.txt"
        user_data = input("Enter some data to write to the new file: ")
        write_file(output_file, user_data)
    else:
        print("No data to write to the new file.")

main()
