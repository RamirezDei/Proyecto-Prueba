import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [tareas, setTareas] = useState([]);
  const [nuevoTitulo, setNuevoTitulo] = useState("");
  const url = "http://127.0.0.1:800/tareas"; // Asegúrate que el puerto sea el correcto

  const cargarTareas = () => {
    axios.get(url).then(res => setTareas(res.data));
  };

  useEffect(() => { cargarTareas(); }, []);

  const agregarTarea = () => {
    const nueva = { id: Date.now(), titulo: nuevoTitulo };
    axios.post(url, nueva).then(() => {
      cargarTareas();
      setNuevoTitulo("");
    });
  };

  const eliminarTarea = (id) => {
    axios.delete(`${url}/${id}`).then(() => cargarTareas());
  };

  const editarTarea = (id) => {
    const tituloEditado = prompt("Nuevo nombre:");
    if (tituloEditado) {
      axios.put(`${url}/${id}`, { id, titulo: tituloEditado }).then(() => cargarTareas());
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Gestor de Tareas</h1>
      <input 
        value={nuevoTitulo} 
        onChange={(e) => setNuevoTitulo(e.target.value)} 
        placeholder="Nueva tarea..." 
      />
      <button onClick={agregarTarea}>Agregar</button>

      <ul>
        {tareas.map(t => (
          <li key={t.id}>
            {t.titulo} 
            <button onClick={() => editarTarea(t.id)}>Editar</button>
            <button onClick={() => eliminarTarea(t.id)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
export default App;