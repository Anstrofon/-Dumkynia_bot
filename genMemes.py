import os
from turtle import width 
from PIL import Image
import random


os.chdir("C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes")


def memes(picture: str):
    os.chdir("C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes")

    def meme1(path: str):

        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("1.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        #picture = picture.resize((widthMeme - 350 , heightMeme - 350))

        if (width > widthMeme and height > heightMeme):
            picture = picture.resize((widthMeme - 350 , heightMeme - 350))
            
        elif(width > widthMeme):
            picture = picture.resize((widthMeme- 350, height))
        elif(height > heightMeme):
            picture = picture.resize((width, heightMeme - 350))

        print(widthMeme - width + (width - widthMeme))
        print(heightMeme - height + (height - heightMeme))
        memeIm.paste(picture,(0, 0) , picture)
        
        print("!!!!!!okey!!!!!!!!!!!!!!")
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))

    def meme2(path: str):

        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("2.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 

        if (width > widthMeme and height > heightMeme):
            picture = picture.resize((widthMeme - 350 , heightMeme - 350))
            #picture.show()
        elif(width > widthMeme):
            picture = picture.resize((widthMeme- 350, height))
        elif(height > heightMeme):
            picture = picture.resize((width, heightMeme - 350))

        print(widthMeme )
        print(heightMeme)
        memeIm.paste(picture,(320, 240) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))

    def meme3(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("3.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((widthMeme - 500 , heightMeme - 550))
        
        print(widthMeme )
        print(heightMeme)
        memeIm.paste(picture,(100, 400) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))

    def meme4(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("4.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((widthMeme - 200 , heightMeme - 350))
    
        print(widthMeme )
        print(heightMeme)
        memeIm.paste(picture,(100, 300) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))
    def meme5(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("5.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((widthMeme - 400 , heightMeme - 250))
    
        print(widthMeme )
        print(heightMeme)
        memeIm.paste(picture,(60, 120) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))
    def meme6(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("6.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((widthMeme  , heightMeme - 400))
    
        print(widthMeme )
        print(heightMeme)
        memeIm.paste(picture,(0, 0) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))

    def meme7(path:str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("7.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((318 , 420))
    
        print(widthMeme)
        print(heightMeme)
        memeIm.paste(picture,(30, 80) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))
    
    
    def meme8(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("8.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((52, 84))
        
        print(widthMeme )
        print(heightMeme)
        memeIm.paste(picture,(167, 23) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))

    def meme9(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("9.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((184 , 443))
       
        memeIm.paste(picture,(90, 0) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))

    def meme10(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("10.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((105 , 62))
        
        print(widthMeme )
        print(heightMeme)
        memeIm.paste(picture,(280, 320) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))

    def meme11(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("11.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((99 , 114))
        
        memeIm.paste(picture,(112, 0) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))

    def meme12(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("12.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((53 , 91))
        
        memeIm.paste(picture,(116, 50) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))

    def meme13(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("13.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((170 , 280))
        
        memeIm.paste(picture,(440, 150) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))
    def meme14(path: str):
        picture = Image.open(path).convert("RGBA")
        memeIm = Image.open("14.jpg")
        widthMeme, heightMeme = memeIm.size

        width, height = picture.size 
        
        picture = picture.resize((95 , 115))
        
        memeIm.paste(picture,(91, 482) , picture)
        
        memeIm.save(os.path.join('C:\\Users\\Anton Yamesow\\Documents\\Rainmeter\\Skins\\Droptop Folders\\CustomFolder1\\pythone ideas\\botik\\Memes\\memed', path))
    
    choice = random.randrange(1, 15)

    match choice:
        case 1:
            meme1(picture)
        case 2:
            meme2(picture)
        case 3:
            meme3(picture)
        case 4:
            meme4(picture)
        case 5:
            meme5(picture)
        case 6:
            meme6(picture)
        case 7:
            meme7(picture)
        case 8:
            meme8(picture)
        case 9:
            meme9(picture)
        case 10:
            meme10(picture)
        case 11:
            meme11(picture)
        case 12:
            meme12(picture)
        case 13:
            meme13(picture)
        case 14:
            meme14(picture)
