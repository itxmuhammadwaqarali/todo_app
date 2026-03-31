import TodoItem from "./TodoItem";

function TodoList({ todos, fetchTodos }) {
  return (
    <div>
      {todos.map((todo) => (
        <TodoItem key={todo.id} todo={todo} fetchTodos={fetchTodos} />
      ))}
    </div>
  );
}

export default TodoList;