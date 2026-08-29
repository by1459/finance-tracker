import type { Transaction } from "../types.ts";

type TransactionRowProps = {
  transaction: Transaction;
};

export function TransactionTable({
  transactions,
}: {
  transactions: Transaction[];
}) {
  return (
    <table>
      <thead>
        <tr>
          <th>Account</th>
          <th>Amount</th>
          <th>Counterparty</th>
          <th>Date</th>
          <th>Category</th>
        </tr>
      </thead>
      <tbody>
        {transactions.map((tx) => (
          <tr key={tx.transactionId}>
            <td>{tx.accountId}</td>
            <td>{tx.transactionId}</td>
            <td>{tx.amount}</td>
            <td>{tx.counterparty}</td>
            <td>{tx.date}</td>
            <td>{tx.category}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
