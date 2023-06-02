
import easyocr

def detecting_image(file_path):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    return result

def main():
    print(detecting_image("photo.png"))

if __name__ == "__main__":
    main()
