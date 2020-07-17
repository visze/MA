import json

with open(snakemake.input.scaffold) as json_file:
    data = json.load(json_file)

    data['data']['dataFile'] = snakemake.input.features
    data['name'] = snakemake.params.name
    data['data']['outFile'] = snakemake.params.output


with open(snakemake.output.config, 'w') as outfile:
    json.dump(data, outfile)
