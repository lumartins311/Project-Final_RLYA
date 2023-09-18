import React, { useEffect, useContext, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Context } from "../store/appContext.js";
import { set } from "date-fns";



export const ListaProf = () => {

    const { store, actions } = useContext(Context);
    const [state, setState] = useState({
        //initialize state here
    });
    const navigate = useNavigate()


    const [prof, setProf] = useState([]);//hice estas constantes
    const [search, setSearch] = useState("");
    const [filtrar, setFiltrar] = useState("");


    const searcher = (e) => {//esta funcion es la que busca
        setSearch(e.target.value)
        console.log(e.target.value)
        }

    const flitro = (e) => {
            setFiltrar(e.target.value)
        }
    const filtrooficio = store.profesionales.filter((oficio) => oficio.id_oficio.name.toLowerCase().includes(filtrar.toLocaleLowerCase()))

    const results = !search & !filtrar ? store.profesionales : search ? store.profesionales.filter((dato) => dato.name.toLowerCase().includes(search.toLocaleLowerCase())) : filtrooficio

  


    useEffect(() => {
        actions.traerInfoProf()
    },[]);
    return (
        <div className=" text-dark list-style-none w-50 p-3">
            
            <form className="d-flex justify-items-center flex-row d-block">
                <div class="dropdown">
                    <button class="btn dropdown-toggle btn-outline-secondary" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                    Filtrar
                    </button>
                        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                            <li><a class="dropdown-item" href="#">Ciudad</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <input type="search" placeholder="Search" aria-label="Search" value={filtrar} onChange={flitro}/>
    
                        </ul>
                </div>
                <input className="form-control me-2 mx-2" type="search" placeholder="Search" aria-label="Search" value={search} onChange={searcher}/>
                <button className="btn btn-outline-secondary" type="submit">Search</button>
            </form>
            <div className="d-block p-2 position-relative">
            <h2>Lista de Profesionales</h2>
                <div className="mx-5 d-flex flex-row">
                    {results.map((item, index) => {
                        return <div className="d-flex flex-column m-3">
                        <img className="rounded-circle" style={{ width: "140px", height: "140px" }} src={item.photo ? item.photo : "https://flyclipart.com/thumb2/usuario-masculino-en-icono-634647.png"} />
                        <a type="button" onClick={()=> navigate("/agenda/" + item.id)} className="btn position-relative rounded-circle">{item.name}</a>
                        </div>
                    })}
                    
                </div>
            </div>
        </div>

    );
};
