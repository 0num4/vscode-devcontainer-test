class Information
  def initialize(animal:, height:)
    @animal, @height = animal, height
  end
end

# TypeProf 0.21.8

# Classes
class Information
    @animal: untyped
    @height: untyped
  
    def initialize: (animal: untyped, height: untyped) -> void
  end