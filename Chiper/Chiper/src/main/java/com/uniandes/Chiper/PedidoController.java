package com.uniandes.Chiper;

import java.util.List;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

@RestController
class PedidoController {

  private final PedidoRepository repository;

  PedidoController(PedidoRepository repository) {
    this.repository = repository;
  }

  // Aggregate root

  @GetMapping("/pedidos")
  public ModelAndView greetingForm(Model model) {
        List<Pedido> allEntries = repository.findAll();
	    model.addAttribute("pedidos", allEntries);
	    return new ModelAndView("pedidos.html");//allEntries.toString();
	  }
//  List<Pedido> all() {
//    return repository.findAll();
//  }
  @GetMapping("/pedidocreate")
  public ModelAndView createPedido(Model model) {
	    return new ModelAndView("pedidocreate.html");//allEntries.toString();
	  }

  @PostMapping("/pedidocreate")
  public ModelAndView addEntry(@RequestParam String name, @RequestParam String role) {
      Pedido newEntry = new Pedido(name, role);
      repository.save(newEntry);
      return new ModelAndView("pedidocreate.html");
  }
//  Pedido newPedido(@RequestBody Pedido newPedido) {
//    return repository.save(newPedido);
//  }

  // Single item

  @GetMapping("/pedidos/{id}")
  Pedido one(@PathVariable Long id) {

    return repository.findById(id)
      .orElseThrow(() -> new PedidoNotFoundException(id));
  }

  @PutMapping("/pedidos/{id}")
  Pedido replacePedido(@RequestBody Pedido newPedido, @PathVariable Long id) {

    return repository.findById(id)
      .map(pedido -> {
        pedido.setName(newPedido.getName());
        pedido.setRole(newPedido.getRole());
        return repository.save(pedido);
      })
      .orElseGet(() -> {
        newPedido.setId(id);
        return repository.save(newPedido);
      });
  }

  @DeleteMapping("/pedidos/{id}")
  void deletePedido(@PathVariable Long id) {
    repository.deleteById(id);
  }
}