
import cv2
import numpy as np
import insightface
from faceindex import FaceIndex



def initialize_insightface_model():
    model = insightface.app.FaceAnalysis()  # Initialize face analysis model
    model.prepare(ctx_id=-1)  # Use GPU (ctx_id=0), or CPU (ctx_id=-1)
    return model


model: insightface.app.FaceAnalysis = initialize_insightface_model()
index: FaceIndex = FaceIndex()

def get_face_embedding_from_frame(model, frame):
    # Detect and extract face embeddings from the captured frame
    faces = model.get(frame)

    if len(faces) > 0:
        embedding = faces[0].normed_embedding  # Get embedding for the first detected face
        return np.array([embedding])  # Convert to a NumPy array for FAISS
    else:
        raise Exception("there is no face")

def get_face_embedding_from_frame(model, frame):
    # frame harus dari opencv
    # Detect and extract face embeddings from the captured frame
    faces = model.get(frame)

    if len(faces) > 0:
        embedding = faces[0].normed_embedding  # Get embedding for the first detected face
        return np.array([embedding])  # Convert to a NumPy array for FAISS
    else:
        print("No face detected in the captured frame.")
        return None

def register_face(frame, label: str):
    array = np.asarray(bytearray(frame), dtype=np.uint8)
    frame = cv2.imdecode(array, cv2.IMREAD_COLOR)
    embedding = get_face_embedding_from_frame(model, frame)
    index.add(embedding, label)


def draw_boundary_face(frame):
    faces = model.get(frame)

    face_count = 0
    for face in faces:
        face_count += 1

        # getting embedding
        embedding = face.normed_embedding  # Get embedding for the first detected face
        embedding = np.array([embedding])

        # search embeding
        distances, indices, labels = index.search(embedding)

        bbox = face.bbox.astype(int)
        topleft = (bbox[0], bbox[1])
        cv2.rectangle(frame, topleft, (bbox[2], bbox[3]), (255, 0, 0), 2)

        # Add the label
        
        if len(labels) > 0:
            label_position = (topleft[0], topleft[1] - 10)
            cv2.putText(frame, labels[0], label_position, cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 2)

        return frame
