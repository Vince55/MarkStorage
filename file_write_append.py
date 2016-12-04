def write_to_file(course_name, table):
    '''
    '''
    file_handle_write = open(course_name + " marks.csv", "w")

    file_handle_write.write("Can\nseparate\nlines\nlike\nthis\n")
    file_handle_write.write("Testing writing function\n")
    file_handle_write.write("Hello friends\n")
    file_handle_write.write("Harambe\n")

    file_handle_write.close()

def append_existing_file(file_name, line):
    '''
    '''
    file_handle_append = open(file_name, "a")
    file_handle_append.write("Adding information to existing file\n")
    file_handle_append.write(line)
    file_handle_append.close()

if (__name__ == "__main__"):
    write_to_file("Computer Science")
    append_existing_file("Computer Science marks.csv", "#Leafs3016")
