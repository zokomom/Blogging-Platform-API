# Blogging-Platform-API
A simple RESTful API with operations for a personal blogging platform.

## Project Description
[Roadmap.sh Blogging Platform API Project Description](https://roadmap.sh/projects/blogging-platform-api)

## Technologies Used
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Postman (for testing)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/zokomom/Blogging-Platform-API.git
cd Blogging-Platform-API
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate.bat
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Set up the database:
- Install PostgreSQL and create a database named `blogging_platform`.
- Update the database connection string in `config.py` if necessary or create a `.env` file with the following content:
```
DATABASE_URL=postgresql://username:password@localhost:5432/blogging_platform
``` 
5. Run the application:
```bash
uvicorn app.main:app --reload
```
## API Endpoints
- Posts:
  - `GET /posts/`: Retrieve a list of all posts.
  - `POST /posts/`: Create a new post.
  - `GET /posts/{post_id}/`: Retrieve a specific post by ID.
  - `PUT /posts/{post_id}/`: Update a specific post by ID.
  - `DELETE /posts/{post_id}/`: Delete a specific post by ID.

## Contributing 🤝🙌
Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

## ❤️ Thank You
Thanks for checking out this project! Feedback and contributions are always appreciated.