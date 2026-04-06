<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class TareaController extends Controller
{
    private $url = 'http://127.0.0.1:800/tareas';

    // Listar tareas
    public function index() {
        $response = Http::get($this->url);
        $tareas = $response->json();
        return view('tareas_python', ['tareas' => $tareas]);
    }

    // Crear tarea
    public function store(Request $request) {
        Http::post($this->url, [
            'id' => rand(1, 999), // ID aleatorio para el ejemplo
            'titulo' => $request->titulo
        ]);
        return redirect()->back()->with('success', 'Tarea creada correctamente');
    }

    // Eliminar tarea
    public function destroy($id) {
        Http::delete($this->url . '/' . $id);
        return redirect()->back()->with('success', 'Tarea eliminada');
    }

    // Editar (Simulación con actualización directa)
    public function update(Request $request, $id) {
        Http::put($this->url . '/' . $id, [
            'id' => $id,
            'titulo' => $request->titulo
        ]);
        return redirect()->back()->with('success', 'Tarea actualizada');
    }
}
