import './App.css'
import { useState } from 'react'


function App() {

  const [amount, setAmount] = useState(0)
  const [category, setCategory] = useState("")
  const [description, setDescription] = usestate("")
  
  return <div className="expense-manager">
    <h1> Expense Manager </h1>
    <h2> Add Expense </h2>

    <label>Amount: <input value={amount} onChange={}/>  </label>
    <label>Category: <input /></label>
    <label>Description: <input /></label>

    <button>Add expense </button>

  </div>
  }



export default App
