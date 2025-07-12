package random;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class InterfaceTest extends JFrame {

    private JButton boton;
    private JLabel etiqueta;

    public InterfaceTest() {
        // Configuración de la ventana
        setTitle("Ejemplo de Interfaz Gráfica");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null); // Layout manual

        // Crear componentes
        etiqueta = new JLabel("Haz clic en el botón");
        etiqueta.setBounds(50, 30, 200, 30);
        add(etiqueta);

        boton = new JButton("Haz clic");
        boton.setBounds(90, 80, 100, 30);
        add(boton);

        // Agregar acción al botón
        boton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                etiqueta.setText("¡Botón presionado!");
            }
        });

        // Hacer visible la ventana
        setVisible(true);
    }

    public static void main(String[] args) {
        // Ejecutar la ventana en el hilo de eventos
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new InterfaceTest();
            }
        });
    }
}
