from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list — resets each time the server restarts
tasks = []
next_id = 1


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks, error=None)


@app.route("/add", methods=["POST"])
def add_task():
    global next_id
    title = request.form.get("task_title", "").strip()

    if not title:
        # Empty submission — show error message
        return render_template(
            "index.html", tasks=tasks,
            error="Task cannot be empty"
        )

    tasks.append({"id": next_id, "title": title})
    next_id += 1
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
