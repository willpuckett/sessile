use regex::Regex;
use std::collections::HashMap;
use std::env;
use std::fs;
use std::path::Path;
use std::error::Error;
use csv::ReaderBuilder;

fn drill_points(min_x: f64, min_hole: f64) -> Result<HashMap<f64, Vec<(f64, f64)>>, Box<dyn Error>> {
    let file_dir = env::var("SESSILE_DIR").unwrap_or_else(|_| env::current_dir()?.to_str().unwrap().to_string());
    let file_path = Path::new(&file_dir).join("case/sessile-drill.drl");
    let drill_text = fs::read_to_string(file_path)?;

    let regex_tools = Regex::new(r"^(T\d+)C(\d+.?\d*)$")?;
    let regex_drills_by_size = Regex::new(r"T\d+(\nX-?\d+.\d+Y-?\d+.\d+)+")?;
    let regex_point = Regex::new(r"^X(-?\d+.\d+)Y(-?\d+.\d+)")?;

    let mut tools = Vec::new();
    for line in drill_text.lines() {
        if let Some(caps) = regex_tools.captures(line) {
            let tool = caps.get(1).unwrap().as_str().to_string();
            let size = caps.get(2).unwrap().as_str().parse::<f64>()?;
            tools.push((tool, if size > min_hole { size } else { min_hole }));
        }
    }

    let mut drills_by_size: HashMap<f64, Vec<(f64, f64)>> = HashMap::new();
    for (tool, size) in &tools {
        drills_by_size.insert(*size, Vec::new());
    }

    for caps in regex_drills_by_size.captures_iter(&drill_text) {
        let lines: Vec<&str> = caps.get(0).unwrap().as_str().trim().split('\n').collect();
        let tool = lines[0];
        let points: Vec<(f64, f64)> = lines[1..]
            .iter()
            .filter_map(|line| {
                regex_point.captures(line).map(|caps| {
                    (
                        caps.get(1).unwrap().as_str().parse::<f64>().unwrap(),
                        caps.get(2).unwrap().as_str().parse::<f64>().unwrap(),
                    )
                })
            })
            .collect();
        if let Some(size) = tools.iter().find(|(t, _)| t == tool).map(|(_, size)| *size) {
            drills_by_size.get_mut(&size).unwrap().extend(points.into_iter().filter(|p| p.0 > min_x));
        }
    }

    drills_by_size.retain(|_, points| !points.is_empty());
    for points in drills_by_size.values_mut() {
        points.sort_unstable();
        points.dedup();
    }

    Ok(drills_by_size)
}

fn locations(ref_designator: Option<&str>) -> Result<HashMap<String, HashMap<String, String>>, Box<dyn Error>> {
    let file_dir = env::var("SESSILE_DIR").unwrap_or_else(|_| env::current_dir()?.to_str().unwrap().to_string());
    let file_path = Path::new(&file_dir).join("sessile_cpl_jlc.csv");
    let mut rdr = ReaderBuilder::new().from_path(file_path)?;

    let mut locations = HashMap::new();
    for result in rdr.deserialize() {
        let record: HashMap<String, String> = result?;
        if let Some(designator) = record.get("Designator") {
            locations.insert(designator.clone(), record);
        }
    }

    if let Some(ref_designator) = ref_designator {
        if let Some(location) = locations.get(ref_designator) {
            let mut single_location = HashMap::new();
            single_location.insert(ref_designator.to_string(), location.clone());
            return Ok(single_location);
        }
    }

    Ok(locations)
}

fn main() -> Result<(), Box<dyn Error>> {
    let drill_points_result = drill_points(0.0, 2.0)?;
    println!("{:?}", drill_points_result);

    let locations_result = locations(Some("SW1"))?;
    println!("{:?}", locations_result);

    Ok(())
}