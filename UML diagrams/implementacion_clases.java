class Libro {
    String idLibro, titulo, autor;
    boolean disponible = true;

    Libro(String id, String t, String a) {
        idLibro = id; titulo = t; autor = a;
    }

    void prestar() {
        if (disponible) { disponible = false; System.out.println("Prestado: " + titulo); }
        else System.out.println("No disponible: " + titulo);
    }

    void devolver() { disponible = true; System.out.println("Devuelto: " + titulo); }
}

class Prestamo {
    String idPrestamo, estado = "Activo";
    Usuario usuario;

    Prestamo(String id, Usuario u) {
        idPrestamo = id; usuario = u;
    }

    void crear(Libro l) { l.prestar(); System.out.println("Préstamo " + idPrestamo + " creado."); }
    void cerrar(Libro l) { estado = "Cerrado"; l.devolver(); System.out.println("Préstamo " + idPrestamo + " cerrado."); }
}

class Usuario {
    String idUsuario, nombre, correo;

    Usuario(String id, String n, String c) {
        idUsuario = id; nombre = n; correo = c;
    }

    void solicitar(Libro l, Prestamo p) { p.crear(l); }
    void devolver(Libro l, Prestamo p) { p.cerrar(l); }

    void mostrarInfo() { System.out.println("Usuario: " + nombre + ", correo: " + correo); }
}

class Bibliotecario extends Usuario { // Herencia
    String idEmpleado, apellido;

    Bibliotecario(String idE, String n, String a) {
        super("N/A", n, "N/A");
        idEmpleado = idE; apellido = a;
    }

    void registrar(Libro l) { System.out.println("Libro '" + l.titulo + "' registrado por " + nombre); }
    void eliminar(Libro l) { System.out.println("Libro '" + l.titulo + "' eliminado por " + nombre); }

    @Override
    void mostrarInfo() { // Polimorfismo
        System.out.println("Bibliotecario: " + nombre + " " + apellido + ", ID: " + idEmpleado);
    }
}

public class Main {
    public static void main(String[] args) {
        Bibliotecario b = new Bibliotecario("001", "Carlos", "Rodriguez");
        Libro libro = new Libro("10", "Cien años de soledad", "Alguien");
        b.registrar(libro);

        Usuario u = new Usuario("001", "Juan", "juan@gmail.com");
        Prestamo p = new Prestamo("01", u);

        u.solicitar(libro, p);
        u.devolver(libro, p);

        // Polimorfismo
        u.mostrarInfo();
        b.mostrarInfo();
    }
}
