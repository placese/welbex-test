import './App.css';
  


const data = [
  { date: "2022-04-03", title: "1st", quantity: 15, distance: 190.5 },
  { date: "2022-04-03", title: "2nd", quantity: 255, distance: 14.55 },
  { date: "2022-04-03", title: "3rd", quantity: 14, distance: 100 },
  { date: "2022-04-03", title: "4th", quantity: 20, distance: 15.6 },
  { date: "2022-04-03", title: "5th", quantity: 13, distance: 24.0 },
]
  
function App() {
  return (
    <div className="App">
      <table>
        <tr>
          <th data-column="date" data-order="desc">Дата</th>
          <th data-column="title" data-order="desc">Название</th>
          <th data-column="quantity" data-order="desc">Количество</th>
          <th data-column="distance" data-order="desc">Расстояние</th>
        </tr>
        {/* {data.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.date}</td>
              <td>{val.title}</td>
              <td>{val.quantity}</td>
              <td>{val.distance}</td>
            </tr>
          )
        })} */}
      </table>
    </div>
  );
}
  
export default App;