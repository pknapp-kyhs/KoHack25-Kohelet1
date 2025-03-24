import tkinter as tk
from searchFunction import Search
lastName = 'Moskowitz'

testing = Search()

def searched(searchValue):
    #import searchFunction as _search
    json_file = "family_docs.json"  # Replace with your actual file
    data = testing.load_json(json_file)
    results = testing.search_json(data, searchValue)

    print("Search Results:", results)
    #upload.upload_family_document()

def tkinterWin():
    global root, logoLabel, welcomeLabel, Search, searchButton, documents, familyTreeButton, backButton, famTreeTestImage, canvas, canvasBack, documentsNotice, infoCanvas, treeMemberDesc, treeMemberName

    # main window
    root = tk.Tk()
    root.title("MySorah")
    root.geometry("400x400")
    root.configure(bg="white")

    # logo on top left/images
    logo = tk.PhotoImage(file="mysorahlogo1.png")
    smallLogo = logo.subsample(15, 15)
    logoLabel = tk.Label(root, image=smallLogo, bd=0)
    logoLabel.place(x=5, y=10, anchor="nw")


    # Labels
    welcomeLabel = tk.Label(root, text="Welcome to MySorah", bg="white", fg="black", font='arial')
    welcomeLabel.pack(pady=15)

    # Buttons
    familyTreeButton = tk.Button(root, text="Family Tree", bg="white", fg="black", font='arial',
                                 width=30, height=2, command=showFamilyTree)
    familyTreeButton.pack(pady=15)

    documents = tk.Button(root, text="Documents", bg="white", fg="black", font='arial', width=30, height=2,
                          command=showUploadDocuments)
    documents.pack()

    # Search functionality
    Search = tk.Entry(root, bg="white", fg="black", font='arial', width=40)
    Search.place(x=0, y=300)

    searchButton = tk.Button(root, text="SEARCH", bg="white", fg="black", font='arial', width=15, height=1,
                             command=lambda: searched(Search.get()))
    searchButton.place(x=115, y=340)

    backButton = tk.Button(root, text="<-", bg="white", fg="black", font='arial', command=showMainMenu)

    # Canvas for family tree
    canvas = tk.Canvas(root, width=400, height=400, bg='white')
    
    canvas.place_forget()  # Initially hidden
    
    canvasBack = tk.Button(canvas, text = '<-', bg='white', fg='black', font='arial', command=showMainMenu)
    canvasBack.place(x=0, y=340)
    infoCanvas = tk.Canvas(root, width=400, height=400, bg='white',borderwidth=0)

    
    treeMemberName = tk.Label(infoCanvas, text="Name: ", bg='white', fg='black', font='arial', width= 20, borderwidth=0, highlightthickness=0)

    treeMemberDesc = tk.Label(infoCanvas, text="Description: ", bg='white', fg='black', font='arial', width= 20, borderwidth=0, highlightthickness=0)

    infoBackButton = tk.Button(infoCanvas, text = '<-', bg='white', fg='black', font='arial', command=showFamilyTree)
    
    
    def showInfo():
        infoBackButton.place(x=0, y=340)
        canvas.place_forget()
        infoCanvas.place(x=0,y=0)
        treeMemberName.pack(padx=100,pady=75)
        treeMemberDesc.pack(padx=100,pady=75)
        
    def AvrumiFunc():
        showInfo()
        
        treeMemberName.config(text = f"Avrumi {lastName}")
        treeMemberDesc.config(text = "Avrumi is a lively \n young bachur who\n excels in the art\n of music. he is a part\n of the family and \nis the eldest of the\n three siblings.")

    def runtFunc():
        showInfo()
        treeMemberName.config(text = f"Runt {lastName}")
        treeMemberDesc.config(text = "Runt is a useless \n child  who\n has no future \n he is a part\n of the family and \nis hated most of\n the three siblings.")

    def brickFunc():
        showInfo()
        treeMemberName.config(text = f"Brick {lastName}")
        treeMemberDesc.config(text = "Brick is a dull \n child who\n was dropped \n as a baby. \nhe is a part\n of the family and \nis the dumbest  of the\n three siblings.")

    def meilechFunc():
        showInfo()
        treeMemberName.config(text = f"Meilech {lastName}")
        treeMemberDesc.config(text = "Meilech is a smart \n rabbi who teaches/ \nlearns Gemara daily.\n he is a part\n of the family and \nis the father of \n Brick, Avrumi, \n and Runt.")

    def strisselFunc():
        showInfo()
        treeMemberName.config(text = f"Strissel {lastName}")
        treeMemberDesc.config(text = "Strissel is a beautiful \n woman who teaches/ \nlearns Navi daily.\n She is a part\n of the family and \nis the mother of \n Brick, Avrumi, \n and Runt.")

    def moisheFunc():
        showInfo()
        treeMemberName.config(text = f"Moishe {lastName}")
        treeMemberDesc.config(text = "Moishe was a nice\n man who fought \nin 'nam.\n He was a part\n of the family and \nis the father of \n  Meilech.")

    def rivkehFunc():
        showInfo()
        treeMemberName.config(text = f"Rivkeh {lastName}")
        treeMemberDesc.config(text = "Rickeh is a beautful \n woman who recently \n lost her hubby.\n She is a part\n of the family and \nis the mother of \n Meilech")

    def dovidFunc():
        showInfo()
        treeMemberName.config(text = f"Dovid {lastName}")
        treeMemberDesc.config(text = "Dovid was a terrible \n person who fought \n on the german \n Side in WWII. \n excomunicated, he \nspent his life \n away from \n the Moskowitzes")

    def malkaFunc():
        showInfo()
        treeMemberName.config(text = f"Malka {lastName}")
        treeMemberDesc.config(text = "Malka was a \n valiant woman who  \nseperated herself\n from Dovid\n After he showed \nhis true colors")
    #infoCanvas.place_forget()
    # Create family tree elements inside the canvas
    def create_member(x, y, name):
        btn = tk.Button(canvas, width=5, height=2)  # Blank button as profile photo
        if name == "Avrumi":
            btn.config(command=AvrumiFunc)
        elif name == "Runt":
            btn.config(command=runtFunc)

        elif name == "Brick":
            btn.config(command=brickFunc)

        elif name == "Meilech":
            btn.config(command=meilechFunc)

        elif name == "Strissel": 
            btn.config(command=strisselFunc)

        elif name == "Moishe":
            btn.config(command=moisheFunc)

        elif name == "Rivkeh":
            btn.config(command=rivkehFunc)

        elif name == "Dovid":
            btn.config(command=dovidFunc)

        elif name == "Malka":
            btn.config(command=malkaFunc)
        btn.place(x=x, y=y)
        lbl = tk.Label(canvas, text=name)
        lbl.place(x=x, y=y + 40)
        return x + 20, y + 20  # Return center position for line drawing
    
    # Grandparents
    gp1_x, gp1_y = create_member(25, 50, "Moishe")
    gp2_x, gp2_y = create_member(100, 50, "Rivkeh")
    gp3_x, gp3_y = create_member(200, 50, "Dovid")
    gp4_x, gp4_y = create_member(275, 50, "Malka")

    # Parents
    p1_x, p1_y = create_member(75, 150, "Meilech")
    p2_x, p2_y = create_member(225, 150, "Strissel")

    # Children
    c1_x, c1_y = create_member(50, 250, "Avrumi")
    c2_x, c2_y = create_member(150, 250, "Runt")
    c3_x, c3_y = create_member(250, 250, "Brick")

    # Family tree photos
    child1 =         tk.PhotoImage(file="familyTreeImages/child1.png")
    child2 = tk.PhotoImage(file="familyTreeImages/child2.png")
    child3 = tk.PhotoImage(file="familyTreeImages/child3.png")

    father = tk.PhotoImage(file="familyTreeImages/man.png")
    mother = tk.PhotoImage(file="familyTreeImages/woman.png")

    grandpa2 = tk.PhotoImage(file="familyTreeImages/grandpa2.png")
    grandpa1 = tk.PhotoImage(file="familyTreeImages/grandpaaa.png")
    grandma1 = tk.PhotoImage(file="familyTreeImages/grandma1.png")
 

    grandma2 = tk.PhotoImage(file="familyTreeImages/grandma2.png")

    # Child Placement
    smallChildOne = child1.subsample(7, 7)
    childOne = tk.Label(canvas, image=smallChildOne, bg="white")
    childOne.place(x=c1_x, y=c1_y - 20)

    smallChildTwo = child2.subsample(13, 13)
    childTwo = tk.Label(canvas, image=smallChildTwo, bg="white")
    childTwo.place(x=c2_x - 10, y=c2_y - 35)
    smallChildThree = child3.subsample(7, 7)
    childThree = tk.Label(canvas, image=smallChildThree, bg="white")
    childThree.place(x=c3_x - 10, y=c3_y - 25)
    #Parent Placement
    
    smallMother = mother.subsample(6, 6)
    motherPhoto = tk.Label(canvas, image=smallMother, bg="white")
    motherPhoto.place(x=p2_x - 10, y=p2_y - 15)

    smallFather = father.subsample(19, 19)
    fatherPhoto = tk.Label(canvas, image=smallFather, bg="white")
    fatherPhoto.place(x=p1_x - 10, y=p1_y - 30)

    #Grandparent Placement
    smallGrandpa1 = grandpa1.subsample(6, 6)
    grandpaOne = tk.Label(canvas, image=smallGrandpa1, bg="white")
    grandpaOne.place(x=gp1_x - 10, y=gp1_y - 15)

    smallGrandma1 = grandma1.subsample(19, 19)
    grandmaOne = tk.Label(canvas, image=smallGrandma1, bg="white")
    grandmaOne.place(x=gp2_x - 10, y=gp2_y - 20)

    smallGrandma2 = grandma2.subsample(22, 22)
    grandmaTwo = tk.Label(canvas, image=smallGrandma2, bg="white")
    grandmaTwo.place(x=gp4_x - 10, y=gp4_y - 15)

    smallGrandpa2 = grandpa2.subsample(25, 25)
    grandpaTwo = tk.Label(canvas, image=smallGrandpa2, bg="white")
    grandpaTwo.place(x=gp3_x - 10, y=gp3_y - 35)


    documentsNotice = tk.Label(root, text="Visit the console to upload documents", bg="white", fg="black", font='arial', width = 50)
    
    
    
    tk.mainloop()


# Functions to hide/show the main menu
def showMainMenu():
    infoCanvas.pack_forget()
    documentsNotice.pack_forget()
    canvas.place_forget()  # Hide the canvas when returning to the main menu
    welcomeLabel.pack(pady=15)
    familyTreeButton.pack(pady=15)
    documents.pack()
    Search.place(x=0, y=300)
    searchButton.place(x=115, y=340)
    backButton.place_forget()

def hideMainMenu():
    documents.pack_forget()
    familyTreeButton.pack_forget()
    welcomeLabel.pack_forget()
    Search.place_forget()
    searchButton.place_forget()
    backButton.place(x=0, y=340)

def showFamilyTree():
    infoCanvas.place_forget()
    canvas.place(x=0, y=0)  # Show the canvas with the family tree
    hideMainMenu()

def showUploadDocuments():
    hideMainMenu()
    documentsNotice.pack(pady=75)


