import { TransactionRow } from './components/transactions.tsx'
import type { Transaction } from './types'

const TRANSACTIONS: Transaction[] = [
	{ accountId: 'acc_1', amount: 1, counterparty: "Tjs", date: 1, categoriy: 'groceries' }
]
export function App() {
	return (<TransactionRow transaction={TRANSACTIONS[0]}/>)
}
