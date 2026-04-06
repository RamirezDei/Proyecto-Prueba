<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Panel de Tareas - Laravel & Python</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 font-sans">

    <div class="container mx-auto py-10 px-4 max-w-2xl">
        <h1 class="text-3xl font-bold text-gray-800 mb-8 text-center">Gestor de Tareas <span class="text-blue-600">Híbrido</span></h1>

        <!-- Formulario para Crear -->
        <div class="bg-white p-6 rounded-lg shadow-md mb-8">
            <form action="{{ route('tareas.store') }}" method="POST" class="flex gap-2">
                @csrf
                <input type="text" name="titulo" placeholder="¿Qué hay que hacer?" required
                    class="flex-1 border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">
                <button type="submit" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-lg transition duration-200">
                    Añadir
                </button>
            </form>
        </div>

        <!-- Lista de Tareas -->
        <div class="bg-white rounded-lg shadow-md overflow-hidden">
            <table class="w-full text-left border-collapse">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-4 font-semibold text-gray-700 uppercase text-xs">Tarea</th>
                        <th class="px-6 py-4 font-semibold text-gray-700 uppercase text-xs text-right">Acciones</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    @foreach($tareas as $tarea)
                    <tr class="hover:bg-gray-50 transition">
                        <td class="px-6 py-4 text-gray-800">
                            {{ $tarea['titulo'] }}
                        </td>
                        <td class="px-6 py-4 flex justify-end gap-2">
                            <!-- Botón Editar (Usa un prompt simple para el ejemplo) -->
                            <button onclick="editar('{{ $tarea['id'] }}', '{{ $tarea['titulo'] }}')" 
                                class="text-yellow-500 hover:text-yellow-600 font-medium text-sm">
                                Editar
                            </button>

                            <!-- Formulario Eliminar -->
                            <form action="{{ route('tareas.destroy', $tarea['id']) }}" method="POST" onsubmit="return confirm('¿Eliminar?')">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="text-red-500 hover:text-red-600 font-medium text-sm">
                                    Eliminar
                                </button>
                            </form>
                        </td>
                    </tr>
                    @endforeach
                </tbody>
            </table>
        </div>
    </div>

    <!-- Formulario oculto para la edición rápida -->
    <form id="edit-form" method="POST" class="hidden">
        @csrf
        @method('PUT')
        <input type="hidden" name="titulo" id="edit-titulo">
    </form>

    <script>
        function editar(id, tituloActual) {
            const nuevoTitulo = prompt("Editar tarea:", tituloActual);
            if (nuevoTitulo && nuevoTitulo !== tituloActual) {
                const form = document.getElementById('edit-form');
                form.action = `/tareas/${id}`;
                document.getElementById('edit-titulo').value = nuevoTitulo;
                form.submit();
            }
        }
    </script>
</body>
</html>