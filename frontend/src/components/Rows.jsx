import React, { useEffect, useState } from "react";
import ReactPaginate from 'react-paginate';


const RowsContext = React.createContext({
    rows: [],
    fetchRows: () => {},
    field_to_sort_by: String,
    order_by: String,
    filter_field: String,
    filter_type: String,
    filter_value: String
});


let field_to_sort_by = "title"
let order_by = "asc"
let filter_field = null
let filter_type = null
let filter_value = null
let slice_start = 0
let slice_stop = 20

export default function Rows() {
    const [rows, setRows] = useState([])
    const fetchRows = async (element = field_to_sort_by, order = order_by) => {
        const response = await fetch("http://localhost:8000/entities?" + new URLSearchParams({
            field_to_sort_by: element,
            order_by: order,
            filter_field: filter_field,
            filter_type: filter_type,
            filter_value: filter_value,
        }))
        const rows = await response.json()
        setRows(rows)
    }
    
    useEffect(() => {
        fetchRows()
    }, [])
    
    const handleClick = (e) => {
        if (field_to_sort_by == e.target.getAttribute('data-column') && order_by == "asc") {
            order_by = "desc"
            field_to_sort_by = e.target.getAttribute('data-column')
            fetchRows()
            return;
        }
        else {
            order_by = "asc"
            field_to_sort_by = e.target.getAttribute('data-column')
            fetchRows()
        }
    }
    
    const filterData = (e) => {
        filter_field = document.getElementById('column-select').value
        filter_type = document.getElementById('condition-select').value
        filter_value = document.getElementById('filter-input').value
        slice_start = 0
        slice_stop = 20
        fetchRows()
    }

    const switchSelectOption = (e) => {
        switch(e.target.value) {
            case "date":
                document.getElementById("condition-above").removeAttribute("disabled")
                document.getElementById("condition-under").removeAttribute("disabled")
                document.getElementById("condition-contains").removeAttribute("disabled")
                break;
            case "title":
                document.getElementById("condition-above").setAttribute("disabled", "disabled")
                document.getElementById("condition-under").setAttribute("disabled", "disabled")
                document.getElementById("condition-contains").removeAttribute("disabled")
                break;
            case "quantity":
                document.getElementById("condition-above").removeAttribute("disabled")
                document.getElementById("condition-under").removeAttribute("disabled")
                document.getElementById("condition-contains").setAttribute("disabled", "disabled")
                break;
            case "distance":
                document.getElementById("condition-above").removeAttribute("disabled")
                document.getElementById("condition-under").removeAttribute("disabled")
                document.getElementById("condition-contains").setAttribute("disabled", "disabled")
                break;
        }
    }

    const handlePageClick = (e) => {
        slice_start = 20 * e.selected
        slice_stop = 20 * (e.selected + 1)
        fetchRows()
    };

    return (
        <div>
        <div className="Content">
        <div className="select">
        <select onChange={switchSelectOption} id="column-select">
            <option value="date">Дата</option>
            <option value="title">Название</option>
            <option value="quantity">Количество</option>
            <option value="distance">Расстояние</option>
        </select>
        <select id="condition-select">
            <option value="equals" id="condition-equals">Равно</option>
            <option value="contains" id="condition-contains">Содержит</option>
            <option value="above" id="condition-above">Больше</option>
            <option value="under" id="condition-under">Меньше</option>
        </select>
        <input id="filter-input" onChange={filterData} />
        </div>
        <div className="Table" id="data-table">
            
            <table>
            <tbody>
            <RowsContext.Provider value={{rows, fetchRows, field_to_sort_by, order_by}}>
            <tr>
                <th data-column="date" data-order="desc">Дата</th>
                <th onClick={handleClick} data-column="title" data-order="desc">Название</th>
                <th onClick={handleClick} data-column="quantity" data-order="desc">Количество</th>
                <th onClick={handleClick} data-column="distance" data-order="desc">Расстояние</th>
            </tr>
                {rows.slice(slice_start, slice_stop).map((val, key) =>(
                    <tr key={key}>
                        <td>{val.date}</td>
                        <td>{val.title}</td>
                        <td>{val.quantity}</td>
                        <td>{val.distance}</td>
                    </tr>
                ))}
            </RowsContext.Provider>
            </tbody>
            </table>
        </div>
        <div id="empty"></div>
        </div>
        <div id="listingTable"></div>
        <ReactPaginate
            breakLabel="..."
            nextLabel="next >"
            onPageChange={handlePageClick}
            pageRangeDisplayed={5}
            pageCount={Math.ceil((rows.length / 20))}
            previousLabel="< previous"
            renderOnZeroPageCount={null}
            containerClassName={'pagination'}
            subContainerClassName={'pages pagination'}
            activeClassName={'active'}
        />
        </div>
    )    
};
