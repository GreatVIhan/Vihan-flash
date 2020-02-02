
import face_recognition
from PIL import Image, ImageDraw #This pillow libary is required for drawing rectangle around the face

pics = fr.load_image_file('/home/vihan/Desktop/sallugroup.jpeg') #Load the Image
face_loc = fr.face_locations(pics) #To find out the number of faces and its count.
print(face_loc)
print("Shreyas")
print(f"There are" {len(face_loc)} "people in this image")

salmankhan = fr.load_image_file('/home/vihan/Desktop/sallu.jpeg')
salmankhan_pic  =  fr.face_encodings(salmankhan)[0]#for encoding the image

known_face_encoding = [salmankhan_pic] #Assign the list to the encoder variable
known_face_name = ["salman khan"]

test_image = fr.load_image_file('/home/vihan/Desktop/sallugroup.jpeg')
face_location = fr.face_locations(test_image)
face_encoding = fr.face_encodings(test_image,face_location)
pil_image = Image.fromarray(test_image)
Draw = ImageDraw.Draw(pil_image)

for(top,right,bottom,left),face_encoding in zip (face_location,face_encoding): #Repeat the same upto all the faces get recognize
    matches  = fr.compare_faces(known_face_encoding,face_encoding)
    name = "Salman Khan"
     if True in matches: #If matches found and got True draw the rectangle and labelled it.
      first_match_index = matches.index(True)
      name = known_face_name[first_match_index]
      Draw.rectangle(((left, top), (right, bottom)), outline=(255,0,0))
      text_width , text_height = Draw.textsize(known_face_name)
      Draw.rectangle(((left,bottom - text_height - 10),(right,bottom)),outline = (97, 149, 232))
      Draw.text((left+6,bottom-text_height-5),name , fill=(5, 247, 247))

del Draw
pil_image.show() #Show the final image.
