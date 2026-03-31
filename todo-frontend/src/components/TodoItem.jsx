import API from "../api/api";

function TodoItem({ todo, fetchTodos }) {
  const complete = async () => {
    try {
      await API.patch(`/todos/${todo.id}`, { completed: !todo.completed });
      fetchTodos();
    } catch (error) {
      alert("Failed to update todo");
    }
  };

  const remove = async () => {
    try {
      await API.delete(`/todos/${todo.id}`);
      fetchTodos();
    } catch (error) {
      alert("Failed to delete todo");
    }
  };

  return (
    <div className={`todo-item ${todo.completed ? "completed" : ""}`}>
      <h3>{todo.title}</h3>
      <p>{todo.task}</p>
      <div className="todo-meta">
        <span className={`priority ${todo.priority}`}>Priority: {todo.priority}</span>
        {todo.due_date && <span>Due: {new Date(todo.due_date).toLocaleString()}</span>}
        <span>Status: {todo.completed ? "Done" : "Pending"}</span>
      </div>
      <div className="todo-actions">
        <button onClick={complete}>
          {todo.completed ? "Mark Pending" : "Complete"}
        </button>
        <button onClick={remove} className="delete">Delete</button>
      </div>
    </div>
  );
}

export default TodoItem;