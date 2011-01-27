var binding = process.binding('evals');

exports.NodeScript = binding.NodeScript;
exports.createScript = function(code, ctx, name) {
  return new exports.NodeScript(code, ctx, name);
};

exports.createContext = binding.NodeScript.createContext;
exports.destroyContext = binding.NodeScript.destroyContext;
exports.runInContext = binding.NodeScript.runInContext;
exports.runInThisContext = binding.NodeScript.runInThisContext;
exports.runInNewContext = binding.NodeScript.runInNewContext;
