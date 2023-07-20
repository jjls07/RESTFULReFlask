import Header from "./components/Header";
import Tasks from "./components/Tasks";
import AddTask from "./components/AddTask";
import { useState } from 'react'

function App() {
  const [showAddTask, setShowAddTask] = useState(false)

  const [tasks, setTasks] = useState([
    {
        id: 1,
        text: 'Cita doctor',
        day: 'Feb 5 a las 2:30PM',
        reminder: true,
    },
    {
        id: 2,
        text: 'Cita dentista',
        day: 'Feb 9 a las 10:30AM',
        reminder: true,
    },
    {
        id: 3,
        text: 'Comprar comida',
        day: 'Feb 14 a las 5:00PM',
        reminder: false,
    },

])

const addTask = (task) => {
  const id = Math.floor(Math.random() * 10000) + 1

  console.log(id)

  const newTask = {id, ...task}
  setTasks([...tasks, newTask])
}

  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id))
  }

  const toggleReminder = (id) => {
    setTasks(tasks.map((task) => task.id === id
    ? {...task, reminder: 
      !task.reminder} : task
    ))
  }

  return (
    <div className="App">
      <Header 
      onAdd={() => setShowAddTask(!showAddTask)}
      showAdd={showAddTask}
      name={ 'Jonathan' }/>
      {showAddTask && 
      <AddTask onAdd={addTask} />}
      {tasks.length > 0 ? ( 
      <Tasks tasks={tasks}
      onDelete = {deleteTask}
      onToggle = {toggleReminder}
      />
      ): (
        'No hay nada para mostar'
      )
    }
    </div>
  );
}

export default App;
