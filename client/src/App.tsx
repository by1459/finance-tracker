import { TransactionTable } from './components/transactions.tsx'
import type { Transaction } from './types'

const TRANSACTIONS: Transaction[] = [
	{ transactionId: 'tsx1', accountId: 'acc_1', amount: 1, counterparty: "Tjs", date: 1, category: 'groceries' }
]
export function App() {
	return (<TransactionTable transactions={TRANSACTIONS}/>)
}
