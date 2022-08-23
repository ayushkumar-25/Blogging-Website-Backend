from fastapi import FastAPI

from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["Blog"])
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get("/blog", response_model=List[schemas.ShowBlog], tags=["Blog"])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get("/blog/{id}", response_model=schemas.ShowBlog, tags=["Blog"])
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id = {id} is nor available")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"detail": f"Blog with id = {id} is nor available"}
#     return blog


# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
# def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with blog id = {id} not found")
#     blog.delete()
#     db.commit()
#     return {"detail": f"Blog with id = {id} has been successfully deleted"}
#
#
# @app.put("/blog/{id}", tags=["Blog"])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with blog id = {id} not found.")
#     blog.update(request.dict())  # {models.Blog.title: request.title, "body": request.body}
#     db.commit()
#     return "Updated"


# @app.post("/user", response_model=schemas.ShowUser, tags=["User"])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email, password=hashing.encrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
#
# @app.get("/user/{id}", response_model=schemas.ShowUser, tags=["User"])
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id = {id} is nor available")
#     return user
