import json




def upload_family_document():
 #   Prompts the user to upload a family document and stores it in a JSON file.
    enteringFileName = True
    file_content = ""
    while enteringFileName:
        file_name = input("Enter the filename (Accepted filetypes include.png, .jpg, and .pdf): ")

        if file_name.lower().endswith(('.png', '.jpg', '.pdf')):
            confirmingFileName = True
            while confirmingFileName:
                fileNameConfirmation = input(f"Confirm the filename:{file_name}? (Y/N): ")
                if fileNameConfirmation.upper() in ["Y","YE","YES"]:
                    # with open(file_name, "rb") as f:
                    #     file_content = f.read()
                    #     enteringFileName = False
                    #     confirmingFileName = False
                    file_content = file_name
                    enteringFileName = False
                    confirmingFileName = False
                elif fileNameConfirmation.upper() in ["N","NO"]:
                    confirmingFileName = False
                else:
                    print("Y/N to confirm the filename")

        else:
            print("Invalid filename. Please enter a filename ending in .png, .jpg, or .pdf.")

    # Get document information
    document_name = input("Enter the name of the document: ")

    document_tag_choice = input("selet a tag: (1) Book, (2) Dvar Torah, (3) Recipe (4) Other: ")

    document_tag = ""
    while document_tag == "":
        if int(document_tag_choice) == 1:
            document_tag = "Book"
        elif int(document_tag_choice) == 2:
            document_tag = "Dvar Torah"
        elif int(document_tag_choice) == 3:
            document_tag = "Recipe"
        elif int(document_tag_choice) ==4:
            document_tag = input("Enter a new tag: ")
        else:
            print("Please assign a tag to the document.")
            document_tag_choice = input("selet a tag: (1) Book, (2) Dvar Torah, (3) Recipe (4) Other: ")

    # Store document data in a JSON file
    documentUploadData = {
        "name": document_name,
        "type": document_tag,
        "content": file_content
    }

    data = []

    with open("./family_docs.json", "r") as f: #copies existing json file data to a list
        data = json.load(f)

    data.append(documentUploadData) #adds new upload data to data, and then dumps it back to the json file
    with open("./family_docs.json", "w") as f:
        json.dump(data, f, indent=4)




    print("Document uploaded successfully!")
