let dataTable
let dataTableIsInitialized=false;

const dataTableOptions={
    columnDefs:[
        {className: "centered", targets:[0, 1, 2, 3, 4, 5, 6] },
        {orderable: false, targets: [5, 6] },
        {searchable: false, targets: [0, 5, 6] },
    ],
    destroy: true
};  

const initDataTable=async()=>{
    if(dataTableIsInitialized){
    dataTable.destroy()
    }

    await listEmpleados();

    dataTable=$('#datatable-empleados').DataTable(dataTableOptions);

    dataTableIsInitialized = true;  
};

const listEmpleados=async()=>{
    try{
        const response=await fetch('http://127.0.0.1:8000/list_empleados/');
        const data = await response.json();

        let content= ``;
        data.tabla.forEach((listEmpleados,tables)=>{
            content += `
                <tr>
                    <td>${tables}</td>
                    <td>${listEmpleados.nombre}</td>
                    <td>${listEmpleados.email}</td>
                    <td>${listEmpleados.telefono}</td>
                    <td>${listEmpleados.cedula}</td>
                    <td>${listEmpleados.password}</td>
                    <td>
                        <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></button>
                        <button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></button>
                    </td>
                </tr>
            `;
        });
        tableBody_empleados.innerHTML = content;
    } catch(ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});