def add(a: Integer, b: Integer)
    return a + b
end
  
  puts add(1, 2)

#   (base) root ➜ /workspaces/vscode-devcontainer-test/rails-with-rbs/rbssample (feat/rails-with-rbs2) $ ruby sample.rb 
# sample.rb:2:in `+': String can't be coerced into Integer (TypeError)

#     return a + b
#                ^
#         from sample.rb:2:in `add'
#         from sample.rb:5:in `<main>'
