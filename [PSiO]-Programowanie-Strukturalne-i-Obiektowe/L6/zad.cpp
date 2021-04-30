#pragma once
#include <iostream>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <functional>

//dot product
template <typename T>
T operator*(std::vector<T> v1, std::vector<T> v2)
{
	if(v1.size()!=v2.size())
	{
		throw std::out_of_range("vectors a and b need to be the same size to calculate the dot product");
	}

	T sum = 0;
	int n = v1.size();

	while (n--)
	{
		sum = (v1[n] * v2[n]) + sum;
	}
	return sum;
}

//complex
template <typename T>
class Complex
{
public:
	T re;
	T im;

	Complex(const T& real = 0, const T& imaginary = 0) :im(imaginary), re(real) {}

	Complex conjugate()
	{
		Complex<T> conj(re, -im);
		return conj;
	}

	T magnitude()
	{
		return std::sqrt(re * re + im * im);
	}

	T angle()
	{
		return std::atan2(im, re);
	}

	void polar()
	{
		std::cout << "z= " << magnitude() << " * exp(" << angle() << "i)";
	}

	void trygonometric()
	{
		std::cout << "z= " << magnitude() << "*cos(" << angle() << ") + i*sin(" << angle() << ")";
	}

	Complex<T> operator/(const Complex<T>& a)
	{
		Complex<T> ret;
		Complex<T> nominator(re * a.re + im * a.im, im * a.re - re * a.im);
		T denominator = a.re * a.re + a.im * a.im;
		ret.re = nominator.re / denominator;
		ret.im = nominator.im / denominator;
		return ret;
	}

	Complex<T> operator*(const Complex<T>& a)
	{
		Complex<T> ret;
		ret.re = re * a.re - im * a.im;
		ret.im = re * a.im + im * a.re;
		return ret;
	}

	friend Complex<T> operator*(const Complex<T>& a, const Complex<T>& b)
	{
		Complex<T> ret;
		ret.re = a.re * b.re - a.im * b.im;
		ret.im = a.re * b.im + a.im * b.re;
		return ret;
	}

	Complex<T>& operator+=(const Complex<T>& b)
	{
		re += b.re;
		im += b.im;
		return *this;
	}

	Complex<T> operator+(Complex<T>& a)
	{
		Complex<T> ret;
		ret.re = re + a.re;
		ret.im = im + a.im;
		return ret;
	}

	Complex<T> operator-(Complex<T>& a)
	{
		Complex<T> ret;
		ret.re = re - a.re;
		ret.im = -im + a.im;
		return ret;
	}

	friend std::ostream& operator<<(std::ostream& os, const Complex<T>& complex)
	{
		os << complex.re << " + " << complex.im << "i";
		return os;
	}
};

//histogram
template <typename T>
class Histogram
{
private:
    std::map<T, int> bins_;
    using T_pair = std::pair<T, int>;

    bool exist(const T& v)
    {
        return bins_.find(v) != bins_.end();
    }

public:
    Histogram(const std::vector<T>& data = std::vector<T>())
    {
        emplace(data);
    }

    void emplace(const T& v)
    {
        if (!exist(v))
        {
            //el not in map => add el to map
            bins_.emplace(T_pair(v, 1));
        }
        else
        {
            //else incr its val
            bins_[v]++;
        }
    }

    void emplace(const std::vector<T>& data)
    {
        for (const auto& v : data)
        {
            emplace(v);
        }
    }

    void clear()
    {
        bins_.clear();
    }

    bool from_csv(const std::string& filename, char delim = ',', int column_idx = 4, bool headers = true)
    {
        //works only when T==string
        std::ifstream csv(filename);
        
        if (!csv.is_open()) { return false; }
        
        std::string temp;

        if (headers)
        {
            //skip first line if file has headers in it;
            std::getline(csv, temp);
        }

        while (std::getline(csv, temp))
        {   
            std::stringstream ss(temp);
            int curr_col_idx = 0;

            while (getline(ss, temp, delim))
            {
                if (curr_col_idx == column_idx)
                {
                    emplace(temp);
                }

                curr_col_idx++;
            }
        }

        csv.close();
        return true;
    }
    
    T_pair max() const
    {
        auto max_ = std::max_element(bins_.begin(), bins_.end(),
            [](T_pair a, T_pair b) 
            {
                return a.second < b.second;
            }
        );

        return *max_;
    }

    std::pair<T, T> range() const
    {
        auto [min_, max_] = std::minmax_element(bins_.begin(), bins_.end(),
            [](T_pair a, T_pair b)
            {
                return a.second < b.second;
            }
        );

        return std::pair<T, T>((*min_).first, (*max_).first);
    }

    std::vector<T_pair> unique_items() const
    {
        std::vector<T_pair> items;
        for (const auto& [v, freq] : bins_)
        {
            items.emplace_back(v, freq);
        }
        return items;
    }

    std::vector<T> unique_bins() const
    {
        std::vector<T> bins;
        for (const auto& [v, freq] : bins_)
        {
            bins.emplace_back(v);
        }
        return bins;
    }

    void print()
    {   
        auto width = 2.5 * max().second;
        std::string hr(width, '-');

        for (const auto& v : bins_)
        {
            std::cout << v.first << ":";
            
            for (int i = 0; i < v.second; i++)
            {
                std::cout << " #";
            }

            std::cout << "\n" << hr << "\n";
        }
    }

    static Histogram generate(int n, T(*get_random_item)())
    {
        Histogram H;
        while (n--)
        {
            H.emplace(get_random_item());
        }
        return H;
    }
};

//matrix
template <typename T>
class Matrix
{
private:
	std::vector<std::vector<T>> mat_;

public:
	Matrix(int rows = 0, int cols = 0) : mat_(rows, std::vector<T>(cols)) {};
	Matrix(std::vector<std::vector<T>> mat) :mat_(mat) {};

	std::pair<int, int> size() const
	{
		return { mat_.size(), mat_[0].size() };
	}

	Matrix transpose() const
	{
		Matrix new_mat(size().second, size().first);
		{
			for (int i = 0; i < size().first; i++)
			{
				for (int j = 0; j < size().second; j++)
				{
					new_mat.mat_[j][i] = mat_[i][j];
				}
			}
		}
		return new_mat;
	}

	static Matrix eye(int rows, int cols)
	{
		Matrix<T> mat(rows,cols);
		for (int i = 0; i < rows; i++)
		{
			for (int j = 0; j < cols; j++)
			{
				if (i == j)
				{
					mat.mat_[i][j] = 1;
				}
			}
		}
		return mat;
	}

	static Matrix fill(int rows, int cols, std::function<T()> gen_num)
	{
		Matrix mat(rows, cols);
		
		for (int i = 0; i < rows; i++)
		{
			for (int j = 0; j < cols; j++)
			{
				mat.mat_[i][j] = gen_num();
			}
		}

		return mat;
	}

	//Stream operators
	friend std::ostream& operator<<(std::ostream& out, Matrix<T>& mat)
	{
		out << "Matrix (" << mat.size().first << ", " << mat.size().second << ") = \n\n";
		for (int i = 0; i < mat.size().first; i++)
		{
			out << "\t\t";
			for (int j = 0; j < mat.size().second; j++)
			{
				out << mat.mat_[i][j] << "\t";
			}
			out << "\n";
		}
		out << "\t";
		return out;
	}

	friend std::istream& operator>>(std::istream& in, Matrix<T>& mat)
	{
		//get_size
		int rows, cols;
		std::cout << "\nMatrix creator:\n\n";
		std::cout << "Enter number of rows: "; in >> rows;
		std::cout << "Enter number of columns: "; in >> cols;

		//fill in matrix
		std::cout << "\nFill in the matrix:\n\n";
		std::vector<std::vector<T>> new_mat;

		for (int i = 0; i < rows; i++)
		{
			std::vector<T> row;
			for (int j = 0; j < cols; j++)
			{
				int el;
				std::cout << "enter element M(" << i + 1 << ", " << j + 1 << "): ";
				in >> el;
				row.emplace_back(el);
			}
			new_mat.emplace_back(row);
		}

		mat.mat_ = new_mat;
		return in;
	}

	//Matrix, Matrix operators
	friend Matrix operator+(Matrix<T> a, const Matrix<T>& b) 
	{
		if (a.size() != b.size())
		{
			throw std::out_of_range("the size of matrices A and B must match in expression A+B");
		}

		for (int i = 0; i < a.size().first; i++)
		{
			for (int j = 0; j < a.size().second; j++)
			{
				a.mat_[i][j] += b.mat_[i][j];
			}
		}

		return a;
	}

	friend Matrix operator-(Matrix<T> a, const Matrix<T>& b) 
	{
		if (a.size() != b.size())
		{
			throw std::out_of_range("the size of matrices A and B must match in expression A-B");
		}

		for (int i = 0; i < a.size().first; i++)
		{
			for (int j = 0; j < a.size().second; j++)
			{
				a.mat_[j][j] -= b.mat_[i][j];
			}
		}

		return a;
	}

	friend Matrix operator*(const Matrix<T>& a, const Matrix<T>& b) 
	{
		//check if can multiply
		if (a.size().second != b.size().first)
		{
			throw std::out_of_range("the number of column in matrix A must match the number of rows in matrix B in expression A*B");
		}

		int new_rows = a.size().first;
		int new_cols = b.size().second;
		Matrix<T> new_mat(new_rows, new_cols);
		for (int i = 0; i < new_rows; i++)
		{
			for (int j = 0; j < new_cols; j++)
			{
				T val = T();
				for (int k = 0; k < a.size().second; k++)
				{
					val += a.mat_[i][k] * b.mat_[k][j];
				}

				new_mat.mat_[i][j] = val;
			}
		}
		
		return new_mat;
	}

	//Matrix, T operators
	friend Matrix operator-(Matrix<T> a, const T& b) 
	{
		for (auto& row : a.mat_)
		{
			for (auto& el : row)
			{
				el -= b;
			}
		}
		return a;
	}

	friend Matrix operator-(const T& b, Matrix<T> a) 
	{
		for (auto& row : a.mat_)
		{
			for (auto& el : row)
			{
				el = b - el;
			}
		}
		return a;
	}

	friend Matrix operator+(Matrix<T> a, const T& b) 
	{
		for (auto& row : a.mat_)
		{
			for (auto& el : row)
			{
				el += b;
			}
		}
		return a;
	}

	friend Matrix operator+(const T& b, Matrix<T> a) 
	{
		return a + b;
	}

	friend Matrix operator*(Matrix<T> a, const T& b) 
	{
		for (auto& row : a.mat_)
		{
			for (auto& el : row)
			{
				el *= b;
			}
		}
		return a;
	}

	friend Matrix operator*(const T& b, Matrix<T> a) 
	{
		return a * b;
	}
};



