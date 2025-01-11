def export_to_file(urls, file_name):
    with open(file_name, 'w') as file:
        for url in urls:
            file.write(url + '\n')
