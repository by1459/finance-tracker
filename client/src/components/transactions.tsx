import type { Transaction } from '../types.ts'

type TransactionRowProps = {
	transaction: Transaction
}

export function TransactionRow({transaction}: TransactionRowProps) {
	return ( 
		<tr>
			<td>{transaction.accountId}</td>
			<td>{transaction.amount}</td>
			<td>{transaction.counterparty}</td>
			<td>{transaction.categoriy}</td>
		</tr>
	)	
}
