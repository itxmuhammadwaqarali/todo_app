import { useEffect, useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/api";
import TodoForm from "../components/TodoForm";
import TodoList from "../components/TodoList";
import FilterBar from "../components/FilterBar";
import { AuthContext } from "../context/AuthContext";

function Dashboard() {
  const [todos, setTodos] = useState([]);
  const [filter, setFilter] = useState("all");
  const { user, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const fetchTodos = async () => {
    try {
      const res = await API.get("/todos");
      setTodos(res.data);
    } catch (error) {
      if (error.response?.status === 401) {
        logout();
        navigate("/");
      }
    }
  };

  useEffect(() => {
    if (!user) {
      navigate("/");
    } else {
      fetchTodos();
    }
  }, [user]);

  const filteredTodos = todos.filter((todo) => {
    if (filter === "completed") return todo.completed;
    if (filter === "pending") return !todo.completed;
    if (filter === "high") return todo.priority === "high";
    return true;
  });

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Todo Dashboard</h1>
        <button onClick={logout}>Logout</button>
      </header>
      <TodoForm fetchTodos={fetchTodos} />
      <FilterBar setFilter={setFilter} />
      <TodoList todos={filteredTodos} fetchTodos={fetchTodos} />
    </div>
  );
}

export default Dashboard;