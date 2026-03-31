import { useState } from "react";
import API from "../api/api";

function TodoForm({ fetchTodos }) {
  const [todo, setTodo] = useState({
    title: "",
    task: "",
    priority: "medium",
    due_date: "",
  });

  const createTodo = async (e) => {
    e.preventDefault();
    try {
      await API.post("/todos", todo);
      setTodo({ title: "", task: "", priority: "medium", due_date: "" });
      fetchTodos();
    } catch (error) {
      alert("Failed to create todo");
    }
  };

  return (
    <form className="todo-form" onSubmit={createTodo}>
      <input
        type="text"
        placeholder="Title"
        value={todo.title}
        onChange={(e) => setTodo({ ...todo, title: e.target.value })}
        required
      />
      <textarea
        placeholder="Task description"
        value={todo.task}
        onChange={(e) => setTodo({ ...todo, task: e.target.value })}
        rows="3"
      />
      <select
        value={todo.priority}
        onChange={(e) => setTodo({ ...todo, priority: e.target.value })}
      >
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>
      <input
        type="datetime-local"
        value={todo.due_date}
        onChange={(e) => setTodo({ ...todo, due_date: e.target.value })}
      />
      <button type="submit">Add Todo</button>
    </form>
  );
}

export default TodoForm;