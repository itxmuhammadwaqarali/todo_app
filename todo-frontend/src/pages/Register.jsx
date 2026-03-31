import { useState } from "react";
import API from "../api/api";
import { useNavigate, Link } from "react-router-dom";

function Register() {
  const [data, setData] = useState({ username: "", password: "" });
  const navigate = useNavigate();

  const register = async (e) => {
    e.preventDefault();
    try {
      await API.post("/register", data);
      navigate("/");
    } catch (error) {
      alert("Registration failed");
    }
  };

  return (
    <div className="auth-container">
      <form className="auth-form" onSubmit={register}>
        <h2>Create Account</h2>
        <input
          type="text"
          placeholder="Username"
          value={data.username}
          onChange={(e) => setData({ ...data, username: e.target.value })}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={data.password}
          onChange={(e) => setData({ ...data, password: e.target.value })}
          required
        />
        <button type="submit">Register</button>
        <p>
          Already have an account? <Link to="/">Login</Link>
        </p>
      </form>
    </div>
  );
}

export default Register;