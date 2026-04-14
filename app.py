from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# In-memory database for rapid prototyping
db = {
    "users": {
        "john@company.com": {"name": "John Doe", "role": "Standard User"}
    }
}

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    rows = "".join([f"<tr><td>{v['name']}</td><td>{k}</td><td>{v['role']}</td></tr>" for k, v in db["users"].items()])
    return f"""
    <html><body>
        <h1>IT Admin Dashboard</h1>
        <nav><a href='/'>Home</a> | <a href='/create'>Create User</a> | <a href='/reset'>Reset Password</a></nav>
        <table border="1">
            <tr><th>Name</th><th>Email</th><th>Role</th></tr>
            {rows}
        </table>
    </body></html>
    """

@app.get("/create", response_class=HTMLResponse)
async def create_form():
    return """
    <html><body>
        <h1>Create New User</h1>
        <form action="/create" method="post">
            <label>Name:</label> <input type="text" name="name"><br>
            <label>Email:</label> <input type="email" name="email"><br>
            <label>Role:</label> <input type="text" name="role"><br>
            <button type="submit">Create</button>
        </form>
        <a href='/'>Back</a>
    </body></html>
    """

@app.post("/create", response_class=HTMLResponse)
async def create_user(name: str = Form(...), email: str = Form(...), role: str = Form(...)):
    db["users"][email] = {"name": name, "role": role}
    return "<h3>User Created Successfully!</h3><a href='/'>Back to Dashboard</a>"

@app.get("/reset", response_class=HTMLResponse)
async def reset_form():
    return """
    <html><body>
        <h1>Reset Password</h1>
        <form action="/reset" method="post">
            <label>User Email:</label> <input type="email" name="email"><br>
            <button type="submit">Send Reset Link</button>
        </form>
        <a href='/'>Back</a>
    </body></html>
    """

@app.post("/reset", response_class=HTMLResponse)
async def reset_password(email: str = Form(...)):
    msg = "Password reset link sent!" if email in db["users"] else "Error: User not found."
    return f"<h3>{msg}</h3><a href='/'>Back to Dashboard</a>"

if __name__ == "__main__":
    # Run the server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)