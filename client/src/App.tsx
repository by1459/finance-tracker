import { useState } from 'react';
import { TransactionTable } from './components/transactions.tsx'
import type { Transaction } from './types'

export function App() {
  const [transactions, setTransactions] = useState<Transaction[]>([])

  async function getTransactions() {
    const res = await fetch('/api/get_transaction')
    const data = await res.json()
    setTransactions([data])
  }

  return (
    <>
      <button onClick={getTransactions}>Load</button>
      <TransactionTable transactions={transactions} />
    </>
  )
}
